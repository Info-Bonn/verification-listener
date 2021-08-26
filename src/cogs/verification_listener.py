import discord
from discord.ext import commands
from discord.ext import tasks

from environment import ROLES, START_CHANNEL, GUILD, NOT_BEFORE, CHECK_PERIOD
from log_setup import logger


class VerificationListener(commands.Cog):
    """
    Give member target roles if member accepts rules screen, check for members that were missed
    """

    def __init__(self, bot: commands.Bot):
        # bot is single server based - for now...
        self.bot = bot
        self.guild: discord.Guild = bot.get_guild(GUILD)
        self.roles = [self.guild.get_role(role) for role in ROLES]
        self.walk_members.start()  # start backup task

    @commands.Cog.listener()
    async def on_member_update(self, before_member: discord.Member, after_member: discord.Member):
        """ Give member target roles if member accepts rules screen """

        if after_member.guild.id != GUILD:
            return

        if before_member.pending and not after_member.pending:
            await after_member.add_roles(*self.roles)

            await after_member.send(self.get_welcome_text(after_member))

    @tasks.loop(minutes=CHECK_PERIOD)
    async def walk_members(self):
        """ Walk all members every five minutes to fix errors that may occurred due to downtimes or other errors """
        logger.info("Executing member check")
        i = 0
        async for member in self.guild.fetch_members():
            # check amount of roles,
            # if member is not pending
            # if he joined after a specific date to not verify old members
            if len(member.roles) == 1 and not member.pending and member.joined_at > NOT_BEFORE:
                await member.add_roles(*self.roles)
                await member.send(self.get_welcome_text(member))
                i += 1

        if i > 0:
            logger.info(f"Verified {i} member that accepted the rules but didn't get the roles")

    def get_welcome_text(self, member: discord.Member):
        return (f"Hey {member.display_name}, willkommen auf dem _{self.guild.name}_ Discord!\n"
                f"Schau für eine kurze Übersicht über den Server gerne mal in "
                f"{self.guild.get_channel(START_CHANNEL).mention} vorbei.\n"
                "Bei Fragen kannst du dich jederzeit an uns wenden,\n"
                "~Die Serverleitung")


def setup(bot: commands.Bot):
    bot.add_cog(VerificationListener(bot))

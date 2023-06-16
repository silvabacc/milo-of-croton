import discord
from discord import ui
from service import insertQuote
from embeds import quote_embed


class AddQuoteModal(ui.Modal, title='Add Quote'):
    quote = ui.TextInput(label='quote', style=discord.TextStyle.paragraph)
    author = ui.TextInput(label='Author')

    async def on_submit(self, interaction: discord.Interaction):
        serializedQuote = self.quote.value
        serializedAuthor = self.quote.value

        result = insertQuote(serializedQuote, serializedAuthor)

        embed = quote_embed(author=serializedAuthor, quote=serializedQuote, id=result["id"])

        await interaction.response.send_message(embed=embed)

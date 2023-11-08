
def min(bot):
	@bot.message_handler(commands=['start'])
	def start(message):

		bot.send_message(message.from_user.id, f"hi, {message.from_user.first_name}! Напиши название города!")



	
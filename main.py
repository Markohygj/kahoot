from negropegro import SQLManager

sql = SQLManager("BaboPotato.db")
sql.create_tables()

sql.add_quizz("Україна","Квіз про Україну")
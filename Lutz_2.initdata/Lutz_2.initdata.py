# Инициализировать данные для последующего сохранения в файлах

#Записи
bob = {'name' : 'Bob Smith', 'age' : 42, 'pay' : 30000, 'job' : 'stw'}
sue = {'name' : 'Sue Jonson', 'age' : 45, 'pay' : 40000, 'job' : 'dev'}
andy = {'name' : 'Andy Near', 'age' : 48, 'pay' : 45000, 'job' : 'dev'}
tom = {'name' : 'Tom Swallow', 'age' : 47, 'pay' : 38000, 'job' : 'stw'}

db  = {}
db['bob'] = bob
db['sue'] = sue
db['andy'] = andy
db['tom'] = tom

if __name__ == '__main__': # проверка переменной __name__  возвра-
                           # щает true, только если файл был запущен как самостоятельный сцена-
                           # рий, а не был импортирован как модуль      
    for key in db:
        print(key, '=>\n', db[key])

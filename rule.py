import db_animal

def import_features(features):
    animal = db_animal.animal
    for xf in features:
        if xf == "有毛发":
            animal.hair = "True"
        if xf == "有奶":
            animal.chest = "True"
        if xf == "有羽毛":
            animal.feather = "True"
        if xf == "会飞":
            animal.fly = "True"
        if xf == "会下蛋":
            animal.lay_eggs = "True"
        if xf == "吃肉":
            animal.meat = "True"
        if xf == "有犀利牙齿":
            animal.tooth = "True"
        if xf == "有爪":
            animal.claw = "True"
        if xf == "眼向前方":
            animal.eye = "True"
        if xf == "有蹄":
            animal.hoof = "True"
        if xf == "反刍":
            animal.ruminate = "True"
        if xf == "有黄褐色":
            animal.color = "Yellow"
        if xf == "有暗斑点":
            animal.speckle = "Dark"
        if xf == "有黑色条纹":
            animal.stripe = "Black"
        if xf == "有长脖子":
            animal.neck = "True"
        if xf == "有长腿":
            animal.leg = "True"
        if xf == "不会飞":
            animal.fly = "False"
        if xf == "有黑白二色":
            animal.color = "Black&white"
        if xf == "会游泳":
            animal.swim = "True"
        if xf == "善飞":
            animal.fly = "Well"
    return animal
def judge(animal):
    Rarr = [False for i in range(8)]
    while True:
        back = False
        #R1：if 动物有毛发  then  动物是哺乳动物
        if Rarr[0]==False and animal.hair == "True":
            animal.mammal = "True"
            Rarr[0] = True #不再执行
            back = True #当前轮次存在符合条件
        #R2：if 动物有奶  then  动物是哺乳动物
        if Rarr[1]==False and animal.chest == "True":
            animal.mammal = "True"
            Rarr[1] = True
            back = True
        #R3：if 动物有羽毛  then  动物是鸟
        if Rarr[2]==False and animal.feather == "True":
            animal.bird = "True"
            Rarr[2] = True
            back = True
        #R4：if 动物会飞 and 会生蛋 then  动物是鸟
        if Rarr[3]==False and animal.fly == "True" and animal.lay_eggs == "True":
            animal.bird = "True"
            Rarr[3] = True
            back = True
        #R5：if 动物吃肉 then 动物是食肉动物
        if Rarr[4]==False and animal.meat == "True":
            animal.carnivore = "True"
            Rarr[4] = True
            back = True
        #R6：if 动物有犀利牙齿 and 有爪 and 眼向前方 then 动物是食肉动物
        if Rarr[5]==False and animal.tooth == "True" and animal.claw == "True" and animal.eye == "True":
            animal.carnivore = "True"
            Rarr[5] = True
            back = True
        #R7：if 动物是哺乳动物and有蹄then动物是有蹄类动物
        if Rarr[6]==False and animal.mammal == "True" and animal.hoof == "True":
            animal.ungulates = "True"
            Rarr[6] = True
            back = True
        #R8：if 动物是哺乳动物and反刍then动物是有蹄类动物
        if Rarr[7]==False and animal.mammal == "True" and animal.ruminate == "True":
            animal.ungulates = "True"
            Rarr[7] = True
            back = True
        #R9：if 动物是哺乳动物and是食肉动物and有黄褐色 and 有暗斑点 then 动物是豹
        if animal.mammal == "True" and animal.carnivore == "True" and animal.color == "Yellow" and animal.speckle == "Dark":
            return "豹"
        #R10：if 动物是哺乳动物 and是食肉动物and有黄褐色 and 有黑色条纹 then 动物是虎
        if animal.mammal == "True" and animal.carnivore == "True" and animal.color == "Yellow" and animal.stripe == "Black":
            return "虎"
        #R11：if动物是有蹄类动物 and 有长脖子and有长腿and有暗斑点 then 动物是长颈鹿
        if animal.ungulates == "True" and animal.neck == "True" and animal.leg == "True" and animal.speckle == "Dark":
            return "长颈鹿"
        #R12：if 动物是有蹄类动物 and有黑色条纹 then 动物是斑马
        if animal.ungulates == "True" and animal.stripe == "Black":
            return "斑马"
        #R13：if 动物是鸟and不会飞 and有长脖子and有长腿 and有黑白二色 then 动物是鸵鸟
        if animal.bird == "True" and animal.neck == "True" and animal.leg == "True" and animal.color == "Black&white":
            return "鸵鸟"
        #R14：if 动物是鸟 and不会飞 and会游泳 and有黑白二色 then  动物是企鹅
        if animal.bird == "True" and animal.fly == "False" and animal.swim == "True" and animal.color == "Black&white":
            return "企鹅"
        #R15：if 动物是鸟 and善飞 then 动物是信天翁
        if animal.bird == "True" and animal.fly == "Well":
            return "信天翁"
        if back==False:#剩下的条件中均不符合
            return

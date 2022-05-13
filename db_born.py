import rule

input_features = input("动物特征(特征以，间隔):")
features_arr = input_features.split('，')  #切割特征
animal = rule.import_features(features_arr) #基本信息
name = rule.judge(animal)
if name:
    print("动物名称:" + name)
else:
    print("暂时无法判断该动物")

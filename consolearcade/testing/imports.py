from rpgFiles import player, enemy, merchant, item

class imports():



    def callMe(self):
        player = player.Player()
        enemy = enemy.Enemy()
        merchant = merchant.Merchant()
        item = item.Item()
        print(player)
        print(enemy)
        print(merchant)
        print(item)
    # print(color.Color().BLACK + item + color.Color().END)

ab = imports()
ab.callMe()
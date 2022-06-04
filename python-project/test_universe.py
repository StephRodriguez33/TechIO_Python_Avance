from universe import count_all_stars
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        count1 = count_all_stars([2, 3])
        assert count1 == 5, "Exécution de count_all_stars([2, 3])... la réponse attendue est 5 mais ton prog. a renvoyé {}".format(count1)
        count2 = count_all_stars([9, -3])
        assert count2 == 6, "Exécution de count_all_stars([9, -3])... la réponse attendue est 6, mais ton prog. a renvoyé {}".format(count2)
        success()

        if sum_builtin_used:
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "_)_/LI")
            send_msg("Bravo, tu es maintenant maitre Yoda. Applaudissement. 🙏", "_)_/LI")
            send_msg("As-tu reconnu le dessin formé au dessus?","")
            send_msg("Yoda",";-)")

        else:
            send_msg("Kudos 🌟", "Saviez-vous que vous pouviez utiliser la fonction somme ? Essayez-la !")
            send_msg("Kudos 🌟", "")
            send_msg("Kudos 🌟", "galaxies = [37, 3, 2]")
            send_msg("Kudos 🌟", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oups! bug! 🐞", e)
        send_msg("Astuce 💡", "Avez-vous correctement accumulé toutes les étoiles dans 'total_stars' ?")


if __name__ == "__main__":
    test_count_all_stars()

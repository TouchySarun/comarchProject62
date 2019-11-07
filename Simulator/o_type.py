def halt(code, g):
    g["pc"] += 1
    g["halt"] = True


def noop(code, g):
    g["pc"] += 1

    


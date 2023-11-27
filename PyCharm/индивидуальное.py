#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"c", "m", "n", "o", "q"}
    b = {"c", "g", "p", "q"}
    c = {"m", "n", "q"}
    d = {"c", "m", "p"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    db = u.difference(b)
    y = (a.intersection(db)).union(c.difference(d))
    print(f"y = {y}")
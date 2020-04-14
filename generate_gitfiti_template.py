#!/usr/bin/env python
import numpy as np
import pprint
import json


def produce_wave_github_graph(period, domain=45, height=7, f=np.sin):
    amplitude = 3.25
    vertical_shift = 3.5

    wave_func = np.round(
        amplitude * f([((2 * np.pi / period) * (n)) for n in range(domain)])
        + vertical_shift
    )

    data = []
    for column, row in enumerate(wave_func):
        data.append([0] * (7 - int(row)) + [2] * (int(row)))

    return np.array(data).transpose()


with open("template", "w") as f:
    sin = produce_wave_github_graph(period=15, f=np.sin)
    cos = produce_wave_github_graph(period=15, f=np.cos)
    print(":sin_cos_wave", file=f)
    f.write(json.dumps((sin + cos).tolist()).replace("],", "],\n"))

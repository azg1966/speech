#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

phrases=[
    ["Товарищи,",
     "С другой стороны",
     "Равным образом",
     "Не следует, однако, забывать",
     "Таким образом",
     "Повседневная практика показывает, что"],

    ["реализация намеченных плановых заданий",
     "рамки и место обучения кадров",
     "постоянный количественный рост и сфера нашей активности",
     "сложившаяся структура организации",
     "новая модель организационной деятельности",
     "дальнейшее развитие различных форм деятельности"],

    ["играет важную роль в формировании",
     "требуют от нас анализа",
     "требуют определения и уточнения",
     "способствует подготовке и реализации",
     "обеспечивает широкому кругу (специалистов) участие в формировании",
     "позволяет выполнить важные задания по разработке"],

    ["существенных финансовых и административных условий.",
     "дальнейших направлений развития.",
     "системы массового участия.",
     "позиций, занимаемых участниками в отношении поставленных задач.",
     "передовых предложений.",
     "направлений прогрессивного развития."]
]

def get_speech(scount):
    speech = []

    for s in range(scount):
        for i in range(4):
            if len(speech) == 0:
                speech.append(phrases[0][0])
            else:
                speech.append(phrases[i][random.randint(0, 5)])

    return ' '.join(speech)

def main():
    print(get_speech(5))

if __name__ == '__main__':
    main()

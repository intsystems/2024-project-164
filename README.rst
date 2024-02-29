|test| |codecov| |docs|

.. |test| image:: https://github.com/intsystems/ProjectTemplate/workflows/test/badge.svg
    :target: https://github.com/intsystems/ProjectTemplate/tree/master
    :alt: Test status
    
.. |codecov| image:: https://img.shields.io/codecov/c/github/intsystems/ProjectTemplate/master
    :target: https://app.codecov.io/gh/intsystems/ProjectTemplate
    :alt: Test coverage
    
.. |docs| image:: https://github.com/intsystems/ProjectTemplate/workflows/docs/badge.svg
    :target: https://intsystems.github.io/ProjectTemplate/
    :alt: Docs status


.. class:: center

    :Название исследуемой задачи: Методы составления эмбеддингов коллекций
    :Тип научной работы: M1P/НИР/CoIS
    :Автор: Парвиз Джурабекович Каримов
    :Научный руководитель: степень, Фамилия Имя Отчество
    :Научный консультант(при наличии): степень, Фамилия Имя Отчество

Abstract
========

Рассматривается задача сопоставления информативных векторных представлений коллекций данных.
Исходный датасет состоит из пар $(x_i, y_i)$, где $x_i \in X$ и $y_i \in \{1, ..., K\}$.
Из точек данных датасета составляются группы $G_{j, k} = \{x_i | (x_i, y_i) \in G \wedge y_i = k \forall i \} : \forall j_1, j_2 G_{j_1, k} \cap G_{j_2, k} = \emptyset$.
Задача состоит в том, чтобы сопоставить каждой группе эмбеддинг $f_{\theta}(G_{j, k})$, представляющий собой информативное векторное представление $G_{j, k}$. 

Research publications
===============================
1. 

Presentations at conferences on the topic of research
================================================
1. 

Software modules developed as part of the study
======================================================
1. A python package *mylib* with all implementation `here <https://github.com/intsystems/ProjectTemplate/tree/master/src>`_.
2. A code with all experiment visualisation `here <https://github.comintsystems/ProjectTemplate/blob/master/code/main.ipynb>`_. Can use `colab <http://colab.research.google.com/github/intsystems/ProjectTemplate/blob/master/code/main.ipynb>`_.

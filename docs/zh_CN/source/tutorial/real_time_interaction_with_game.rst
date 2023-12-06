实时游玩
##########################################

GoBigger 允许用户在个人电脑中实时游玩。同时也提供了多种游戏模式供用户选择。

.. note::

    如果你还在使用 GoBigger v0.1.x 系列，建议升级以获得更好的体验。可以使用 ``pip install --upgrade gobigger`` 来快速获取最新版本的 GoBigger。


标准比赛模式+部分视野
=======================

该模式下，玩家只能看到周围一定范围内的视野。可以通过以下代码启动游戏：

.. code-block:: bash

    python -m gobigger.bin.play --mode st --vision-type partial

在本模式中，鼠标可以用来操控玩家控制的球，三个技能分别是 ``Q``，``W``。``Q`` 技能是在移动方向上吐孢子，``W`` 技能是将用户的球进行分裂。玩家的视野由球的相对位置决定。尝试分散玩家的球，这样可以获得更大的视野。


标准比赛模式+全局视野
=======================

可以通过以下代码启动游戏：

.. code-block:: bash

    python -m gobigger.bin.play --mode st --vision-type full


独立动作比赛模式+部分视野
=======================

独立动作比赛模式下，玩家的每个球都单独接受一个动作。但是由于比较难操控，我们在这个模式下还是只根据鼠标和键盘接收一个动作，并将这个动作赋给玩家的所有球。可以通过以下代码来启动游戏：

.. code-block:: bash

    python -m gobigger.bin.play --mode sp --vision-type partial

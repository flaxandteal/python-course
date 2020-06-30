Magnum Opus
===========

Recipe maker for the philosopher's stone.


    python3 -m pytest --cov magnumopus >> README.md

    ============================= test session starts ==============================
    platform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /home/philtweir/Work/Training/PythonCourse/python-course/022-burette/magnum_opus
    plugins: pep8-1.0.6, cov-2.10.0
    collected 15 items

    tests/domain/test_alembic.py .......                                     [ 46%]
    tests/domain/test_pantry.py ..                                           [ 60%]
    tests/domain/test_substance.py ......                                    [100%]

    ----------- coverage: platform linux, python 3.8.2-final-0 -----------
    Name                                                 Stmts   Miss  Cover
    ------------------------------------------------------------------------
    magnumopus/__init__.py                                  10      8    20%
    magnumopus/config.py                                     4      4     0%
    magnumopus/index.py                                      2      2     0%
    magnumopus/initialize.py                                 6      6     0%
    magnumopus/logger.py                                     4      4     0%
    magnumopus/models/__init__.py                            3      1    67%
    magnumopus/models/base.py                                2      0   100%
    magnumopus/models/substance.py                          24      0   100%
    magnumopus/repositories/__init__.py                      0      0   100%
    magnumopus/repositories/pantry.py                       12      1    92%
    magnumopus/repositories/sqlalchemy_pantry.py            15     15     0%
    magnumopus/resources/__init__.py                         7      7     0%
    magnumopus/resources/alembic_instruction.py             26     26     0%
    magnumopus/resources/substance.py                       28     28     0%
    magnumopus/schemas/__init__.py                           4      4     0%
    magnumopus/schemas/substance_schema.py                  11     11     0%
    magnumopus/services/__init__.py                          0      0   100%
    magnumopus/services/alembic.py                          32      2    94%
    magnumopus/services/alembic_instruction_handler.py      20     20     0%
    magnumopus/services/assessor.py                          2      2     0%
    ------------------------------------------------------------------------
    TOTAL                                                  212    141    33%


    ============================== 15 passed in 0.38s ==============================

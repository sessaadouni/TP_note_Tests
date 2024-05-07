import pytest

from task import TaskList, TaskStatus
from exception import InvalidTransition

def test_create_list_object():
    tl = TaskList("Create Task")
    assert tl.name == "Create Task"

def test_create_task():
    tl = TaskList("Les courses")
    # la priorité par défaut sera 10
    tl.create_task(name="Acheter du beurre")
    assert "Acheter du beurre" in tl.get_all_task_names()

def test_get_task():
    tl = TaskList("Les courses")
    tl.create_task(name="Acheter de la margarine", priority=1)
    task = tl.get_task_by_name("Acheter de la margarine")
    assert task.priority == 1
    tl.create_task(name="Acheter des fleurs", priority=5)
    p5_tasks = tl.get_tasks_by_priority(5)
    task_1 = p5_tasks[0]
    assert task_1.name == 'Acheter des fleurs'
    # vérifier que la priorité par défaut est 10 quand on ne met pas de priorité
    tl.create_task("Acheter une assiette")
    task_assiette = tl.get_task_by_name("Acheter une assiette")
    assert task_assiette.priority == 10

def test_manage_tasks_1():
    tl = TaskList("Ménage")
    tl.create_task(name="Ranger la chambre", priority=6)
    tl.create_task(name="Faire la vaisselle", priority=6)
    # on vérifie qu'une tâche nouvellement créée possède le statut "TODO"
    ranger = tl.get_task_by_name("Ranger la chambre")
    assert ranger.status == TaskStatus.TODO
    # on vérifie que le statut DONE se reflète bien sur la tâche dans la liste
    ranger.set_status(TaskStatus.DONE)
    ranger_2 = tl.get_task_by_name("Ranger la chambre")
    assert ranger.status == TaskStatus.DONE
    assert ranger_2.status == TaskStatus.DONE

def test_manage_tasks_2():
    # On va créer et annuler des éléments dans une liste de tâches
    tl = TaskList("Les courses")
    tasks_to_create = ["Acheter des oranges", "Acheter des pommes"]
    for t in tasks_to_create:
      tl.create_task(t)
    # on vérifie que toutes nos tâches ont bien été créées
    all_task_names = tl.get_all_task_names()
    assert set(all_task_names) == set(tasks_to_create)
    # on annule les pommes
    task_pommes = tl.get_task_by_name("Acheter des pommes")
    task_pommes.set_status(TaskStatus.CANCELED)
    # on vérifie que les pommes sont bien annulées
    all_task_names = tl.get_all_task_names()
    assert 'Acheter des pommes' not in all_task_names

def test_manage_tasks_3():
    # On vérifie qu'une tâche CANCELED ne peut pas être marquée DONE
    tl = TaskList("Les courses")
    tasks_to_create = ["Acheter des oranges", "Acheter des pommes"]
    for t in tasks_to_create:
      tl.create_task(t)
    task_pommes = tl.get_task_by_name("Acheter des pommes")
    task_pommes.set_status(TaskStatus.CANCELED)
    with pytest.raises(InvalidTransition):
      task_pommes.set_status(TaskStatus.DONE)
    # le statut ne doit pas avoir changé
    assert task_pommes.status == TaskStatus.CANCELED
    # on vérifie que la tâche CANCELED peut être remise en statut TODO
    task_pommes.set_status(TaskStatus.TODO)
    assert task_pommes.status == TaskStatus.TODO
    # maintenant on va marquer la tâche DONE et cela doit marcher
    task_pommes.set_status(TaskStatus.DONE)
    assert task_pommes.status == TaskStatus.DONE
    # on vérifie dans la TaskList aussi
    pommes_2 = tl.get_task_by_name("Acheter des pommes")
    assert pommes_2.status == TaskStatus.DONE

def test_show_tasks():
    EXAMPLE_OUTPUT =( "== Ménage ==\n"
                      "[1] Faire la vaisselle\n"
                      "[1] Ranger la cuisine\n"
                      "[2] Balayer le couloir\n"
                      "Total: 3")
    EXAMPLE_OUTPUT_LINES = EXAMPLE_OUTPUT.split('\n')
    tl = TaskList("Ménage")
    tl.create_task("Faire la vaisselle", priority=1)
    tl.create_task("Balayer le couloir", priority=2)
    tl.create_task("Ranger la cuisine", priority=1)
    tl.create_task("Repeindre la porte", priority=10)
    tl.get_task_by_name("Repeindre la porte").set_status(TaskStatus.CANCELED)
    result = str(tl)
    print(result)
    result_split = result.split('\n')
    # On teste le titre
    assert result_split[0] == EXAMPLE_OUTPUT_LINES[0]
    # On teste que chacune des lignes attendues dans la mise en page
    # est bien présente
    for line in EXAMPLE_OUTPUT_LINES:
      print("Is", line, 'there?')
      assert line in result
    # On teste que la sortie est exactement la même que l'exemple
    assert result == EXAMPLE_OUTPUT

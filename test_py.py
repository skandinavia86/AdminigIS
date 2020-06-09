  
import pytest
import app
import os.path

# Тест на создание БД (1)
# Тест на наличие столбцов в Clients (2)
# Тест на наличие столбцов в Orders #(3)
# Тест на наличие 10 строк в Clients (4)
# Тест на наличие 10 строк в Orders (5)

def test_create_database(): #(1)
    app.init_db()
    assert os.path.exists(app.db_name) == True

def test_clients(): #(2)
    assert app.Clients.name == True
    assert app.Clients.city == True
    assert app.Clients.address == True

def test_orders():  #(3)
    assert app.Orders.clients == True
    assert app.Orders.amount ==True
    assert app.Orders.date == True
    assert app.Orders.description == True

def test_sum_clients(): #(4)
    app.fill_db()
    assert len(app.Clients.select()) > 9

def test_sum_orders(): #(5)
    assert len(app.Orders.select()) > 9

# Coffee Maker (OOP)

## What it does

A command-line coffee machine simulation. Orders espresso, latte, or cappuccino; accepts coin input; tracks resources and profit; prints a report on demand.

## Key concepts

- Class design and single-responsibility separation
- Inter-object method calls (`CoffeeMaker` checks resources, `MoneyMachine` handles payment)
- Class attributes vs instance attributes

## How it works

Three classes handle distinct concerns: `Menu`/`MenuItem` define available drinks and their costs, `CoffeeMaker` tracks ingredient inventory and deducts on each order, `MoneyMachine` processes coin input and tracks profit. `main.py` wires them together in a loop.

## How to run

```
$ python main.py
```

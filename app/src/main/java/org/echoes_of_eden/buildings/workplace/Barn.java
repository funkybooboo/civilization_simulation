package main.java.org.echoes_of_eden.buildings.workplace;

import java.util.ArrayList;

public class Barn extends Workplace {
    protected ArrayList<Firewood> firewood;
    protected ArrayList<Wood> wood;
    protected ArrayList<Coal> coal;
    protected ArrayList<Stone> stone;
    protected ArrayList<Iron> iron;
    protected ArrayList<Tool> tools;
    protected ArrayList<Food> food;
    protected ArrayList<Clothes> clothes;
    
    public Barn() {
        this.stoneRequired = 10;
        this.woodRequired = 10;
        this.ironRequired = 10;

        this.stoneDelivered = 0;
        this.woodDelivered = 0;
        this.ironDelivered = 0;

        this.firewood = new ArrayList<Firewood>();
        this.wood = new ArrayList<Wood>();
        this.coal = new ArrayList<Coal>();
        this.stone = new ArrayList<Stone>();
        this.iron = new ArrayList<Iron>();
        this.tools = new ArrayList<Tool>();
        this.food = new ArrayList<Food>();
        this.clothes = new ArrayList<Clothes>();

        this.numberOfWorkers = 0;
        this.maxWorkers = 20;

        this.isUsable = false;
    }

    public void disaster() {
        // implement disaster
    }

}
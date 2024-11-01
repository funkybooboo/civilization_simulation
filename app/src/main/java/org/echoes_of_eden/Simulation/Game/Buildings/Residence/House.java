package org.echoes_of_eden.Simulation.Game.Buildings.Residence;

public class House extends Residence {

    public House() {
        this.stoneRequired = 10;
        this.woodRequired = 10;
        this.ironRequired = 10;

        this.stoneDelivered = 0;
        this.woodDelivered = 0;
        this.ironDelivered = 0;

        this.isUsable = false;

        this.food = new ArrayList<Food>();
        this.firewood = new ArrayList<Firewood>();
        this.coal = new ArrayList<Coal>();
    }

    public void disaster() {
        // implement disaster
    }
}

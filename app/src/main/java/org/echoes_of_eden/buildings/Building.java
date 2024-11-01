package main.java.org.echoes_of_eden.buildings;

abstract class Building {
    protected int stoneRequired;
    protected int stoneDelivered;
    protected int woodRequired;
    protected int woodDelivered;
    protected int ironRequired;
    protected int ironDelivered;
    protected boolean isUsable;

    public abstract void disaster();
}
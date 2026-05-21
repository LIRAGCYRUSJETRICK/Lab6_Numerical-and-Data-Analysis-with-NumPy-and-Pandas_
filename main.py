
    df_anim = df.iloc[::10].reset_index(drop=True)
    times   = df_anim["timestamp"].dt.strftime("%H:%M")

    # ── Animation 1: Sensor 1 builds over time ────────────────
    fig, ax = plt.subplots(figsize=(10, 4))
    line, = ax.plot([], [], color="#2196F3", linewidth=1.5)
    ax.set_xlim(0, len(df_anim))
    ax.set_ylim(df_anim["sensor_1_temp_C"].min() - 0.5,
                df_anim["sensor_1_temp_C"].max() + 0.5)
    ax.set_title("Sensor 1 Temperature Over Time — July 1, 2025")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.axhline(df_anim["sensor_1_temp_C"].mean(), color="red",
               linestyle="--", alpha=0.5, label="Mean")
    ax.legend()

    # Show only every 20th x-tick so labels don't overlap
    tick_positions = range(0, len(df_anim), 20)
    ax.set_xticks(list(tick_positions))
    ax.set_xticklabels([times[i] for i in tick_positions], rotation=45, fontsize=7)

    def update1(frame):
        line.set_data(range(frame), df_anim["sensor_1_temp_C"].values[:frame])
        return line,

    ani1 = animation.FuncAnimation(
        fig, update1, frames=len(df_anim),
        interval=50, blit=True
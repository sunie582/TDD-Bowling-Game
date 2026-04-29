# Habit Tracker System

## Overview
Folder contains the complete set of UML diagrams for the **Habit Tracker** project.

## Diagrams and Documentation

### 1. Functional Requirements
* **Use Case Diagram (`habit.jpg`)**
    * **Actors:** User,Administrator.
    * **Key Features:** User registration (with email validation), habit management, marking habits as complete (updating streaks), and viewing progress history. Administrators can manage users and system logs.

### 2. System Architecture
* **Class Diagram (`Class diagram HabitTracker.jpg`)**
    * **Core Classes:** User, Habit, HabitLog, Achievement, Dashboard.
    * **Relationships:** Illustrates composition between `Habit` and `HabitLog`, and dependency between `Habit` and the `Dashboard` for report generation.

### 3. Behavioral Modeling
* **Activity Diagram (`ACTIVITY DIAGRAM habit.jpg`)**
    * Maps the logic of marking a habit as "Done", including checks for archived status and achievement triggers.
* **Sequence Diagram (`SEQUENCE DIAGRAM habit.jpg`)**
    * Shows the step-by-step interaction between the Dashboard, Habit, and Achievement objects when a user records progress.
* **State Machine Diagram (`STATE DIAGRAM habit.jpg`)**
    * Tracks the lifecycle of a habit: from `Created` and `Active` to `Complete for today`, `Pending` (next day), or `Archived/Deleted`.

## Technical Goals
- Model a scalable object-oriented structure for habit tracking.
- Define clear interaction sequences for daily user activities.
- Implement business logic for streaks and gamification (achievements).

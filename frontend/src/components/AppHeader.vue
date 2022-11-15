<template>
    <header>
        <h1>{{title}}</h1>
        <!-- IF showAddTask == False ? 'Close' else : 'AddTask' ??? -->
        <!-- <Button v-show="homePage" @btn-click="$emit('toggle-add-task')" :text="showAddTask ? 'Close' : 'Add Task'" :color="showAddTask ? 'red' : 'green'" /> -->
        <!-- <Button text="Update Task" color="blue" />
        <Button text="Delete Task" color="red" /> -->


    </header>
</template>

<script>

export default {
    name: 'AppHeader',
    props: {
        title: String,
    },
}
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;

    }
</style>
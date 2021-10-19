<template>
    <div class="container">
        <div class="columns">
            <div class="column is-one-quarter">
                <Sidebar />
            </div>
            <div class="column">
                <h1 class="title">Users</h1>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'

export default {
    name: 'Users',
    components: {
        Sidebar,
    },
}
</script>

<style>
</style>
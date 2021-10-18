<template>
    <b-navbar id="nav">
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <p>Poolsnap</p>
            </b-navbar-item>
        </template>
        <template #start> </template>

        <template #end>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button is-primary">
                        <strong>Sign up</strong>
                    </a>
                    <a class="button is-light"> Log in </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<style scoped>
</style>
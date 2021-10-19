<template>
    <b-menu>
        <b-menu-list>
            <router-link :to="{ name: 'Overview' }">
                <b-menu-item
                    icon="information-outline"
                    label="Overview"
                ></b-menu-item>
            </router-link>
            <b-menu-item icon="settings" :active="isActive" expanded>
                <template #label="props">
                    Administrator
                    <b-icon
                        class="is-pulled-right"
                        :icon="props.expanded ? 'menu-up' : 'menu-down'"
                    ></b-icon>
                </template>
                <router-link :to="{ name: 'Users' }">
                    <b-menu-item icon="account" label="Users"></b-menu-item>
                </router-link>
                <b-menu-item icon="cellphone-link">
                    <template #label>
                        Devices
                        <b-dropdown
                            aria-role="list"
                            class="is-pulled-right"
                            position="is-bottom-left"
                        >
                            <template #trigger>
                                <b-icon icon="dots-vertical"></b-icon>
                            </template>
                            <b-dropdown-item aria-role="listitem"
                                >Action</b-dropdown-item
                            >
                            <b-dropdown-item aria-role="listitem"
                                >Another action</b-dropdown-item
                            >
                            <b-dropdown-item aria-role="listitem"
                                >Something else</b-dropdown-item
                            >
                        </b-dropdown>
                    </template>
                </b-menu-item>
                <b-menu-item
                    icon="cash-multiple"
                    label="Payments"
                    disabled
                ></b-menu-item>
            </b-menu-item>
            <b-menu-item icon="account" label="My Account">
                <b-menu-item label="Account data"></b-menu-item>
                <b-menu-item label="Addresses"></b-menu-item>
            </b-menu-item>
        </b-menu-list>
        <b-menu-list>
            <b-menu-item
                label="Expo"
                icon="link"
                tag="router-link"
                target="_blank"
                to="/expo"
            ></b-menu-item>
        </b-menu-list>
    </b-menu>
</template>

<script>
export default {
    data() {
        return {
            isActive: true,
        }
    },
}
</script>
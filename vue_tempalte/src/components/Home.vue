<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">

            Чат на Vue.JS
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
            <mu-button flat slot="right" v-else @click="logOut">Выход</mu-button>
        </mu-appbar>

<!--        <mu-row>-->
<!--            <Room v-if @openDialog="openDialog"></Room>-->

<!--            <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>-->

<!--        </mu-row>-->
        <slot></slot>
    </mu-container>
</template>

<script>
    // import Room from "./rooms/Room"
    // import Dialog from "./rooms/Dialog";

    export default {
        name: "Home",
        // components: {
        //     Room,
        //     Dialog
        // },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false
                }
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logOut() {
                sessionStorage.removeItem("auth_token")
                window.location = "/"
            },
            // openDialog(id) {
            //     this.dialog.id = id;
            //     this.dialog.show = true
            // }
        },
    }
</script>

<style scoped>

</style>

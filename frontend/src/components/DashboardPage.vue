<template>
    <div id="container">
        <div id="navbar">
            <div id="app-banner">
                <h2>AquaEasy</h2>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('AnalysisComponent')">Dashboard</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('HistoricalData')">Archive</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('FaqPage')">FAQs</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="changeComponent('ProfilePage')">Profile</h4>
            </div>

            <div class="nav-link">
                <img src="" alt="" class="nav-link-icon">
                <h4 @click="this.$router.push('Login')">Log Out</h4>
            </div>
        </div>

        <div id="main-content">
            <component :is="currentComponent" />
        </div>
    </div>
</template>

<script>
import HistoricalData from './HistoricalData.vue';
import AnalysisComponent from './AnalysisComponent.vue';
import FaqPage from './FaqPage.vue';
import ProfilePage from './ProfilePage.vue';
import LoginPage from './LoginPage.vue';

export default {
    name: 'DashboardPage',
    components: {
        HistoricalData,
        AnalysisComponent,
        FaqPage,
        LoginPage,
        ProfilePage
    },  
    methods: {
        changeComponent(componentName){
            this.currentComponent = componentName;
        }
    },
    data(){
        return {
            currentComponent: 'HistoricalData'
        }
    }
}
</script>

<style scoped lang="scss">
#container {
        height: 100vh;
        width: 100vw;
        display: flex;
        position: absolute;
        top: 0;
        left: 0;
    }

    #navbar {
        width: 220px;
        min-width: 220px;
        background-color: #333;
        color: white;
        padding: 20px;
        box-sizing: border-box;
    }

    .nav-link {
        margin-bottom: 15px;
        cursor: pointer;
    }

    #main-content {
        overflow-y: scroll;
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        box-sizing: border-box;
    }
</style>
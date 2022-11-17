import { createStore } from 'vuex'
import axios from 'axios';
import router from "../router";

export default createStore({
    state: {
        accessToken: '',
        refreshToken: '',
        expiration: Date.now(),
        isBusy: false,
        error: "",
    },
    mutations: {
        setBusy: (state) => state.isBusy = true,
        clearBusy: (state) => state.isBusy = false,
        setError: (state, error) => state.error = error,
        clearError: (state) => state.error = "",
        setToken: (state, model) => {
            state.accessToken = 'Bearer ' + model.tokens.access;
            state.refreshToken = model.tokens.refesh;
            state.expiration = new Date(model.expiration)
        },
        clearToken: (state) => {
            state.accessToken = "";
            state.expiration = Date.now();
        }
    },
    getters: {
        isAuthenticated: (state) => state.accessToken.length > 0 && state.expiration > Date.now()
    },
    actions: {
        register: async ({ commit }, model) => {
            try {
                const result = await axios.post('auth/signup/', model);
                if (result.data.message) {
                    router.push("/login");
                }
                else {
                    commit("setError", "Authentication Failed");
                }
            } catch {
                commit("setError", "Failed to register");
            } finally {
                commit("clearBusy");
            }
        },
        login: async ({ commit }, model) => {
            try {
                const result = await axios.post('auth/login/', model);
                if (result.data.message === "Login Successfull") {
                    commit("setToken", result.data);
                    router.push("/dashboard");
                }
                else {
                    console.log(result.data.message)
                    commit("setError", "Authentication Failed");
                }
            } catch {
                commit("setError", "Failed to login");
            } finally {
                commit("clearBusy");
            }
        },
        logout: ({ commit }) => {
            commit("clearToken");
            router.push("/");
        },
    }
})
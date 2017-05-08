"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var http_1 = require("@angular/http");
var settings_1 = require("../settings");
var HttpClient = (function () {
    function HttpClient(http) {
        this.http = http;
    }
    HttpClient.prototype.createAuthorizationHeader = function (headers) {
        var token = localStorage.getItem(settings_1.Settings.LOCAL_STORAGE_TOKEN_KEY);
        var keyword;
        if (!token)
            return;
        if (token.length == settings_1.Settings.NORMAL_API_TOKEN_LENGTH) {
            keyword = settings_1.Settings.NORMAL_API_TOKEN_KEYWORD;
        }
        else if (token.length == settings_1.Settings.SOCIAL_API_TOKEN_LENGTH) {
            keyword = settings_1.Settings.SOCIAL_API_TOKEN_KEYWORD;
        }
        else {
            console.log('Error. API token has unnexpected length!', token);
            return;
        }
        headers.append('Authorization', keyword + ' ' + token);
    };
    HttpClient.prototype.get = function (url, params) {
        if (params === void 0) { params = new http_1.URLSearchParams(); }
        var headers = new http_1.Headers();
        this.createAuthorizationHeader(headers);
        return this.http.get(url, {
            headers: headers,
            search: params
        });
    };
    HttpClient.prototype.post = function (url, data) {
        var headers = new http_1.Headers();
        this.createAuthorizationHeader(headers);
        return this.http.post(url, data, {
            headers: headers
        });
    };
    return HttpClient;
}());
HttpClient = __decorate([
    core_1.Injectable()
], HttpClient);
exports.HttpClient = HttpClient;

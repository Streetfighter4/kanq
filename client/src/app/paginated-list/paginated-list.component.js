"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var settings_1 = require("../settings");
var PaginatedListComponent = (function () {
    function PaginatedListComponent() {
        this.elements = [];
        this.currentPage = 0;
        this.perPage = settings_1.Settings.ELEMENTS_PER_PAGE;
        this.shouldScroll = true;
    }
    PaginatedListComponent.prototype.onScroll = function () {
        if (this.shouldScroll)
            this.loadNextPage(this.currentPage, this.perPage);
    };
    PaginatedListComponent.prototype.ngOnInit = function () {
        this.loadNextPage(this.currentPage, this.perPage);
    };
    PaginatedListComponent.prototype.addPage = function (newElements) {
        this.elements = this.elements.concat(newElements);
        this.currentPage++;
        if (newElements.length == 0)
            this.shouldScroll = false;
        if (this.shouldScroll)
            this.loadNextPage(this.currentPage, this.perPage);
    };
    PaginatedListComponent.prototype.loadNextPage = function (perPage, currentPage) { };
    return PaginatedListComponent;
}());
PaginatedListComponent = __decorate([
    core_1.Component({
        selector: 'paginated-list',
        template: '',
    })
], PaginatedListComponent);
exports.PaginatedListComponent = PaginatedListComponent;

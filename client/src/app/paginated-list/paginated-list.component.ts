import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Settings} from '../settings';

@Component({
  selector: 'paginated-list',
  template: '',
})
export class PaginatedListComponent<T> implements OnInit {
  elements: T[] = [];
  currentPage: number = 0;
  perPage: number = Settings.ELEMENTS_PER_PAGE;
  shouldScroll: boolean = true;

  constructor() { }

  onScroll() {
    if(this.shouldScroll)
        this.loadNextPage(this.currentPage, this.perPage);
  }

  ngOnInit() {
    this.loadNextPage(this.currentPage, this.perPage);
  }

  addPage(newElements: T[]) {
    this.elements = this.elements.concat(newElements);
    this.currentPage++;

    if(newElements.length == 0)
      this.shouldScroll = false;

    if(this.shouldScroll)
      this.loadNextPage(this.currentPage, this.perPage);
  }

  loadNextPage(perPage: number, currentPage: number) {}
}


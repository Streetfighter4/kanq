import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PaginatedListComponent } from './paginated-list.component';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule
  ],
  declarations: [
    PaginatedListComponent
  ],
  exports: [
    PaginatedListComponent
  ]
})
export class PaginatedListModule { }

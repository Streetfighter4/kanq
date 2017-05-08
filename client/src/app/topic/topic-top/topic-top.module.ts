import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';
import {TopicTopComponent} from './topic-top.component';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule,
    RouterModule
  ],
  declarations: [
    TopicTopComponent
  ],
  exports: [
    TopicTopComponent
  ]
})
export class TopicTopModule { }

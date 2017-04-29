import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicDetailComponent} from './topic-detail.component';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [
    TopicDetailComponent
  ],
  exports: [
    TopicDetailComponent
  ]
})
export class TopicDetailModule { }

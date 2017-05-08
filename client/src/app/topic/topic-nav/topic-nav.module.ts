import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TopicNavComponent } from './topic-nav.component';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [
    TopicNavComponent
  ],
  exports: [
    TopicNavComponent
  ]
})
export class TopicNavModule { }

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PostGlanceComponent } from './post-glance.component';
import {RouterModule} from '@angular/router';
import {RatingModule} from '../../rating/rating.module';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    RatingModule
  ],
  declarations: [
    PostGlanceComponent
  ],
  exports: [
    PostGlanceComponent
  ]
})
export class PostGlanceModule { }

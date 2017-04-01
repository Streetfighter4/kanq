import {RouterModule, Routes} from '@angular/router';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {NgModule} from '@angular/core';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';

const routes: Routes = [
  {path: 'oauth/facebook/authorize', component: FacebookAuthorizerComponent},
  {path: 'oauth/facebook/token', component: FacebookTokenHandlerComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}

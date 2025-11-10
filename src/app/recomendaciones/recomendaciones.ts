import { Component, inject } from '@angular/core';
import { Product, RecommendationService } from '../services/recommendation-service';

@Component({
  selector: 'app-recomendaciones',
  standalone: false,
  templateUrl: './recomendaciones.html',
  styleUrl: './recomendaciones.css',
})
export class Recomendaciones {

  private dataService = inject(RecommendationService);

  public products: Product[] = [];

  ngOnInit(): void {
    this.dataService.getPosts().subscribe(datos => {
      this.products = datos;
      console.log(this.products);
    });
  }































































    title1 = 'Maxi york Hacendado finas lonchas'
    title2 = 'Cerdo a tacos'
    title3 = 'Chuletas lomo de cerdo'
}

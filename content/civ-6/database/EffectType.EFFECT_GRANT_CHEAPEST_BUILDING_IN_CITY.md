---
tags:
- EffectType
title: EFFECT_GRANT_CHEAPEST_BUILDING_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_CHEAPEST_BUILDING_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_ADJUST_NON_CAPITAL_FREE_CHEAPEST_BUILDING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_NON_CAPITAL_FREE_CHEAPEST_BUILDING",
		"MODIFIER_PLAYER_CITIES_GRANT_CHEAPEST_BUILDING_IN_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_NON_CAPITAL_FREE_CHEAPEST_BUILDING",
		"Amount",
		1
	);
	
```


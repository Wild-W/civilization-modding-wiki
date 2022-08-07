---
tags:
- EffectType
title: EFFECT_ADJUST_FORBID_LAND_ROUTE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FORBID_LAND_ROUTE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Domestic `Unknown`

## Samples

```SQL {title="TRAIT_FORBID_INTERNATIONAL_LAND_ROUTES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FORBID_INTERNATIONAL_LAND_ROUTES",
		"MODIFIER_PLAYER_ADJUST_FORBID_LAND_ROUTE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FORBID_INTERNATIONAL_LAND_ROUTES",
		"Domestic",
		0
	);
	
```


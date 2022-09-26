---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_PROJECTS_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_PROJECTS_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MINOR_CIV_HONG_KONG_PROJECT_PRODUCTION_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_HONG_KONG_PROJECT_PRODUCTION_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_ALL_PROJECTS_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_HONG_KONG_PROJECT_PRODUCTION_BONUS",
		"Amount",
		20
	);
	
```

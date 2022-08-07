---
tags:
- EffectType
title: EFFECT_CITY_GRANT_RANDOM_RESOURCE_PRODUCT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_CITY_GRANT_RANDOM_RESOURCE_PRODUCT
>
> * Class: `Unknown`
> * Parameters:
>	* ResourceType `Unknown`

## Samples
```SQL {title="PROJECT_COMPLETION_CREATE_CORPORATION_PRODUCT_HONEY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PROJECT_COMPLETION_CREATE_CORPORATION_PRODUCT_HONEY",
		"MODIFIER_PLAYER_GRANT_RANDOM_RESOURCE_PRODUCT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_CREATE_CORPORATION_PRODUCT_HONEY",
		"ResourceType",
		"RESOURCE_HONEY"
	);
	
```


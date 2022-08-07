---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_RESOURCE_ACCUMULATION_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_RESOURCE_ACCUMULATION_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>		* Amount to adjust the extra accumulation modifier.
>	* ResourceType `String`
>		* If no resource type is specified\, the modifier applies to all accumulatable resources.
>		* [Resources.ResourceType]

## Samples

```SQL {title="EQUESTRIAN_ORDERS_ADDITIONAL_HORSES_EXTRACTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EQUESTRIAN_ORDERS_ADDITIONAL_HORSES_EXTRACTION",
		"MODIFIER_PLAYER_ADJUST_RESOURCE_ACCUMULATION_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EQUESTRIAN_ORDERS_ADDITIONAL_HORSES_EXTRACTION",
		"Amount",
		1
	),
	(
		"EQUESTRIAN_ORDERS_ADDITIONAL_HORSES_EXTRACTION",
		"ResourceType",
		"RESOURCE_HORSES"
	);
	
```


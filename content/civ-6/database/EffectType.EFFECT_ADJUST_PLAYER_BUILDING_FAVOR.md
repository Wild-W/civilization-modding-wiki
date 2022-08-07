---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_BUILDING_FAVOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_BUILDING_FAVOR
>
> * Class: `PLAYERS`
> * Parameters:
>	* BuildingType `String`
>	* Favor `Integer`

## Samples

```SQL {title="DISINFORMATION_CAMPAIGN_BROADCAST_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DISINFORMATION_CAMPAIGN_BROADCAST_FAVOR",
		"MODIFIER_PLAYER_ADJUST_BUILDING_FAVOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DISINFORMATION_CAMPAIGN_BROADCAST_FAVOR",
		"BuildingType",
		"BUILDING_BROADCAST_CENTER"
	),
	(
		"DISINFORMATION_CAMPAIGN_BROADCAST_FAVOR",
		"Favor",
		3
	);
	
```


---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_DIPLOMATIC_VICTORY_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_DIPLOMATIC_VICTORY_POINTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Tooltip `String`
>	* VictoryResolution `Boolean`

## Samples

```SQL {title="STATUELIBERTY_DIPLOVP"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"STATUELIBERTY_DIPLOVP",
		"MODIFIER_PLAYER_ADJUST_DIPLOMATIC_VICTORY_POINTS",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STATUELIBERTY_DIPLOVP",
		"Amount",
		4
	),
	(
		"STATUELIBERTY_DIPLOVP",
		"Tooltip",
		"LOC_DVP_TOOLTIP_OTHER_SOURCES"
	);
	
```


```SQL {title="ADD_DIPLOMATIC_VICTORY_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ADD_DIPLOMATIC_VICTORY_POINTS",
		"MODIFIER_PLAYER_ADJUST_DIPLOMATIC_VICTORY_POINTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ADD_DIPLOMATIC_VICTORY_POINTS",
		"Amount",
		2
	),
	(
		"ADD_DIPLOMATIC_VICTORY_POINTS",
		"Tooltip",
		"LOC_DVP_TOOLTIP_DVP_RESOLUTION"
	),
	(
		"ADD_DIPLOMATIC_VICTORY_POINTS",
		"VictoryResolution",
		1
	);
	
```


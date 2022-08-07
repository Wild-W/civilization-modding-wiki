---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FAVOR_REFUND_FOR_SUCCESSFUL_RESOLUTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FAVOR_REFUND_FOR_SUCCESSFUL_RESOLUTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Percent `Integer`
>	* ResolutionType `String`
>		* [Resolutions.ResolutionType]
>	* WhichEffect `Integer`
>		* 1>		  2

## Samples

```SQL {title="FUTURE_COUNTER_DIPLOMATIC_REFUND_VP_RESOLUTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FUTURE_COUNTER_DIPLOMATIC_REFUND_VP_RESOLUTION",
		"MODIFIER_PLAYER_ADJUST_FAVOR_REFUND_FOR_SUCCESSFUL_RESOLUTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FUTURE_COUNTER_DIPLOMATIC_REFUND_VP_RESOLUTION",
		"Percent",
		50
	),
	(
		"FUTURE_COUNTER_DIPLOMATIC_REFUND_VP_RESOLUTION",
		"ResolutionType",
		"WC_RES_DIPLOVICTORY"
	),
	(
		"FUTURE_COUNTER_DIPLOMATIC_REFUND_VP_RESOLUTION",
		"WhichEffect",
		2
	);
	
```


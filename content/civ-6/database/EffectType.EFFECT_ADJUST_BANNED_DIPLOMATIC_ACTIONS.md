---
tags:
- EffectType
title: EFFECT_ADJUST_BANNED_DIPLOMATIC_ACTIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BANNED_DIPLOMATIC_ACTIONS
>
> * Class: `Unknown`
> * Parameters:
>	* Banned `Boolean`
>	* DiplomaticActionType `String`
>		* [DiplomaticActions.DiplomaticActionType]

## Samples

```SQL {title="TRAIT_NO_SUPRISE_WAR_FOR_CANADA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NO_SUPRISE_WAR_FOR_CANADA",
		"MODIFIER_PLAYER_ADJUST_BANNED_DIPLOMATIC_ACTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NO_SUPRISE_WAR_FOR_CANADA",
		"Banned",
		1
	),
	(
		"TRAIT_NO_SUPRISE_WAR_FOR_CANADA",
		"DiplomaticActionType",
		"DIPLOACTION_DECLARE_SURPRISE_WAR"
	);
	
```


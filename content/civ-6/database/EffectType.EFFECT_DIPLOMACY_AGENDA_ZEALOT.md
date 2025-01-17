---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_ZEALOT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_ZEALOT
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomRankingDiploMod `Integer`
>	* HiddenAgenda `Boolean`
>	* StatementKey `String`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_ZEALOT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_ZEALOT",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_ZEALOT",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_ZEALOT",
		"BottomRankingDiploMod",
		"-6"
	),
	(
		"AGENDA_ZEALOT",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_ZEALOT",
		"StatementKey",
		"AGENDA_ZEALOT_WARNING"
	),
	(
		"AGENDA_ZEALOT",
		"TopRankingDiploMod",
		6
	);
	
```


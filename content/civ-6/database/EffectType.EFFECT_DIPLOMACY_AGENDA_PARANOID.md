---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_PARANOID
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_PARANOID
>
> * Class: `PLAYERS`
> * Parameters:
>	* HiddenAgenda `Boolean`
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_PARANOID"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_PARANOID",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_PARANOID",
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
		"AGENDA_PARANOID",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_PARANOID",
		"StatementKey",
		"AGENDA_PARANOID_WARNING"
	);
	
```


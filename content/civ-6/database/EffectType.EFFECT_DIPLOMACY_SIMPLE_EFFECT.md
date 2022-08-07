---
tags:
- EffectType
title: EFFECT_DIPLOMACY_SIMPLE_EFFECT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_SIMPLE_EFFECT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Accumulates `Boolean`
>	* DiplomacyKey `String`
>	* HiddenAgenda `Boolean`
>	* IncrementTurns `Integer`
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* MaxValue `Integer`
>	* MessageThrottle `Integer`
>	* OnlyOwnersCity `Boolean`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_CULTURE_BOMBED"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_CULTURE_BOMBED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"Accumulates",
		1
	),
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"InitialValue",
		"-10"
	),
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"ReductionTurns",
		10
	),
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"ReductionValue",
		"-1"
	),
	(
		"STANDARD_DIPLOMATIC_CULTURE_BOMBED",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_CULTURE_BOMBED"
	);
	
```

```SQL {title="STANDARD_DIPLOMATIC_CONVERTED_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_CITY_CONVERTED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"DiplomacyKey",
		"WARNING_STOP_CONVERTING_MY_CITIES"
	),
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"InitialValue",
		"-9"
	),
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"MessageThrottle",
		20
	),
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"ReductionTurns",
		10
	),
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"ReductionValue",
		"-1"
	),
	(
		"STANDARD_DIPLOMATIC_CONVERTED_CITY",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_CITY_CONVERTED"
	);
	
```

```SQL {title="AGENDA_CLEARS_BARBARIAN_CAMPS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_CLEARS_BARBARIAN_CAMPS",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_CLEARS_BARBARIAN_CAMPS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_CLEARS_BARBARIAN_CAMPS",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_CLEARS_BARBARIAN_CAMPS",
		"InitialValue",
		6
	),
	(
		"AGENDA_CLEARS_BARBARIAN_CAMPS",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_DESCRIPTION_ATTACKS_BARBARIANS"
	),
	(
		"AGENDA_CLEARS_BARBARIAN_CAMPS",
		"StatementKey",
		"LOC_DIPLO_KUDO_LEADER_ANY_REASON_AGENDA_ATTACKS_BARBARIANS"
	);
	
```

```SQL {title="AGENDA_BACKSTAB_AVERSE_FRIEND"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_DECLARED_FRIEND"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"IncrementTurns",
		10
	),
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"IncrementValue",
		1
	),
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"InitialValue",
		1
	),
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"MaxValue",
		12
	),
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_BACKSTAB_AVERSE_FRIEND"
	),
	(
		"AGENDA_BACKSTAB_AVERSE_FRIEND",
		"StatementKey",
		"LOC_DIPLO_KUDO_LEADER_TOMYRIS_REASON_ANY"
	);
	
```

```SQL {title="AGENDA_ALLY_OF_ENKIDU_FRIEND"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_DECLARED_FRIEND"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"InitialValue",
		12
	),
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"MessageThrottle",
		20
	),
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"ReductionTurns",
		10
	),
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"ReductionValue",
		1
	),
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_ALLY_OF_ENKIDU_DECLARED_FRIEND"
	),
	(
		"AGENDA_ALLY_OF_ENKIDU_FRIEND",
		"StatementKey",
		"LOC_DIPLO_KUDO_LEADER_GILGAMESH_REASON_ANY"
	);
	
```

```SQL {title="STANDARD_DIPLOMATIC_OCCUPIED_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_OCCUPIED_CITY",
		"MODIFIER_PLAYER_DIPLOMACY_SIMPLE_MODIFIER",
		"PLAYER_CITY_OCCUPIED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_OCCUPIED_CITY",
		"InitialValue",
		"-18"
	),
	(
		"STANDARD_DIPLOMATIC_OCCUPIED_CITY",
		"OnlyOwnersCity",
		1
	),
	(
		"STANDARD_DIPLOMATIC_OCCUPIED_CITY",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_CITY_OCCUPIED"
	);
	
```

